import { Component, Vue, Inject } from 'vue-property-decorator';

import { required } from 'vuelidate/lib/validators';

import AlertService from '@/shared/alert/alert.service';

import UserService from '@/entities/user/user.service';

import CarritoService from '@/entities/carrito/carrito.service';
import { ICarrito } from '@/shared/model/carrito.model';

import { ICliente, Cliente } from '@/shared/model/cliente.model';
import ClienteService from './cliente.service';
import { Genero } from '@/shared/model/enumerations/genero.model';

const validations: any = {
  cliente: {
    genero: {
      required,
    },
    telefono: {
      required,
    },
    direccion1: {
      required,
    },
    direccion2: {},
    ciudad: {
      required,
    },
    pais: {
      required,
    },
    user: {
      required,
    },
  },
};

@Component({
  validations,
})
export default class ClienteUpdate extends Vue {
  @Inject('clienteService') private clienteService: () => ClienteService;
  @Inject('alertService') private alertService: () => AlertService;

  public cliente: ICliente = new Cliente();

  @Inject('userService') private userService: () => UserService;

  public users: Array<any> = [];

  @Inject('carritoService') private carritoService: () => CarritoService;

  public carritos: ICarrito[] = [];
  public generoValues: string[] = Object.keys(Genero);
  public isSaving = false;
  public currentLanguage = '';

  beforeRouteEnter(to, from, next) {
    next(vm => {
      if (to.params.clienteId) {
        vm.retrieveCliente(to.params.clienteId);
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
    if (this.cliente.id) {
      this.clienteService()
        .update(this.cliente)
        .then(param => {
          this.isSaving = false;
          this.$router.go(-1);
          const message = this.$t('deliveryApp.cliente.updated', { param: param.id });
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
      this.clienteService()
        .create(this.cliente)
        .then(param => {
          this.isSaving = false;
          this.$router.go(-1);
          const message = this.$t('deliveryApp.cliente.created', { param: param.id });
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

  public retrieveCliente(clienteId): void {
    this.clienteService()
      .find(clienteId)
      .then(res => {
        this.cliente = res;
      })
      .catch(error => {
        this.alertService().showHttpError(this, error.response);
      });
  }

  public previousState(): void {
    this.$router.go(-1);
  }

  public initRelationships(): void {
    this.userService()
      .retrieve()
      .then(res => {
        this.users = res.data;
      });
    this.carritoService()
      .retrieve()
      .then(res => {
        this.carritos = res.data;
      });
  }
}
