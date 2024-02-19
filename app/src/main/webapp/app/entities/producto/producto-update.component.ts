import { Component, Inject } from 'vue-property-decorator';

import { mixins } from 'vue-class-component';
import JhiDataUtils from '@/shared/data/data-utils.service';

import { required } from 'vuelidate/lib/validators';

import AlertService from '@/shared/alert/alert.service';

import ProductoCategoriaService from '@/entities/producto-categoria/producto-categoria.service';
import { IProductoCategoria } from '@/shared/model/producto-categoria.model';

import ProductoOrdenService from '@/entities/producto-orden/producto-orden.service';
import { IProductoOrden } from '@/shared/model/producto-orden.model';

import { IProducto, Producto } from '@/shared/model/producto.model';
import ProductoService from './producto.service';
import { Medida } from '@/shared/model/enumerations/medida.model';

const validations: any = {
  producto: {
    nombre: {
      required,
    },
    description: {},
    medida: {
      required,
    },
    image: {},
    productoCategoria: {
      required,
    },
  },
};

@Component({
  validations,
})
export default class ProductoUpdate extends mixins(JhiDataUtils) {
  @Inject('productoService') private productoService: () => ProductoService;
  @Inject('alertService') private alertService: () => AlertService;

  public producto: IProducto = new Producto();

  @Inject('productoCategoriaService') private productoCategoriaService: () => ProductoCategoriaService;

  public productoCategorias: IProductoCategoria[] = [];

  @Inject('productoOrdenService') private productoOrdenService: () => ProductoOrdenService;

  public productoOrdens: IProductoOrden[] = [];
  public medidaValues: string[] = Object.keys(Medida);
  public isSaving = false;
  public currentLanguage = '';

  beforeRouteEnter(to, from, next) {
    next(vm => {
      if (to.params.productoId) {
        vm.retrieveProducto(to.params.productoId);
      }
      vm.initRelationships();
    });
  }

  created(): void {
    this.currentLanguage = this.$store.getters.currentLanguage;
    this.$store.watch(
      () => this.$store.getters.currentLanguage,
      () => {
        this.currentLanguage = this.$store.getters.currentLanguage;
      }
    );
  }

  public save(): void {
    this.isSaving = true;
    if (this.producto.id) {
      this.productoService()
        .update(this.producto)
        .then(param => {
          this.isSaving = false;
          this.$router.go(-1);
          const message = this.$t('deliveryApp.producto.updated', { param: param.id });
          return this.$root.$bvToast.toast(message.toString(), {
            toaster: 'b-toaster-top-center',
            title: 'Info',
            variant: 'info',
            solid: true,
            autoHideDelay: 5000,
          });
        })
        .catch(error => {
          this.isSaving = false;
          this.alertService().showHttpError(this, error.response);
        });
    } else {
      this.productoService()
        .create(this.producto)
        .then(param => {
          this.isSaving = false;
          this.$router.go(-1);
          const message = this.$t('deliveryApp.producto.created', { param: param.id });
          this.$root.$bvToast.toast(message.toString(), {
            toaster: 'b-toaster-top-center',
            title: 'Success',
            variant: 'success',
            solid: true,
            autoHideDelay: 5000,
          });
        })
        .catch(error => {
          this.isSaving = false;
          this.alertService().showHttpError(this, error.response);
        });
    }
  }

  public retrieveProducto(productoId): void {
    this.productoService()
      .find(productoId)
      .then(res => {
        this.producto = res;
      })
      .catch(error => {
        this.alertService().showHttpError(this, error.response);
      });
  }

  public previousState(): void {
    this.$router.go(-1);
  }

  public clearInputImage(field, fieldContentType, idInput): void {
    if (this.producto && field && fieldContentType) {
      if (Object.prototype.hasOwnProperty.call(this.producto, field)) {
        this.producto[field] = null;
      }
      if (Object.prototype.hasOwnProperty.call(this.producto, fieldContentType)) {
        this.producto[fieldContentType] = null;
      }
      if (idInput) {
        (<any>this).$refs[idInput] = null;
      }
    }
  }

  public initRelationships(): void {
    this.productoCategoriaService()
      .retrieve()
      .then(res => {
        this.productoCategorias = res.data;
      });
    this.productoOrdenService()
      .retrieve()
      .then(res => {
        this.productoOrdens = res.data;
      });
  }
}
