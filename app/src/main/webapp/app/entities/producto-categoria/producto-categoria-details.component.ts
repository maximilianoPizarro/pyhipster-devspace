import { Component, Vue, Inject } from 'vue-property-decorator';

import { IProductoCategoria } from '@/shared/model/producto-categoria.model';
import ProductoCategoriaService from './producto-categoria.service';
import AlertService from '@/shared/alert/alert.service';

@Component
export default class ProductoCategoriaDetails extends Vue {
  @Inject('productoCategoriaService') private productoCategoriaService: () => ProductoCategoriaService;
  @Inject('alertService') private alertService: () => AlertService;

  public productoCategoria: IProductoCategoria = {};

  beforeRouteEnter(to, from, next) {
    next(vm => {
      if (to.params.productoCategoriaId) {
        vm.retrieveProductoCategoria(to.params.productoCategoriaId);
      }
    });
  }

  public retrieveProductoCategoria(productoCategoriaId) {
    this.productoCategoriaService()
      .find(productoCategoriaId)
      .then(res => {
        this.productoCategoria = res;
      })
      .catch(error => {
        this.alertService().showHttpError(this, error.response);
      });
  }

  public previousState() {
    this.$router.go(-1);
  }
}
