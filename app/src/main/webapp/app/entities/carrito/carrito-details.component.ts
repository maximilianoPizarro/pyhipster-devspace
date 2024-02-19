import { Component, Vue, Inject } from 'vue-property-decorator';

import { ICarrito } from '@/shared/model/carrito.model';
import CarritoService from './carrito.service';
import AlertService from '@/shared/alert/alert.service';

@Component
export default class CarritoDetails extends Vue {
  @Inject('carritoService') private carritoService: () => CarritoService;
  @Inject('alertService') private alertService: () => AlertService;

  public carrito: ICarrito = {};

  beforeRouteEnter(to, from, next) {
    next(vm => {
      if (to.params.carritoId) {
        vm.retrieveCarrito(to.params.carritoId);
      }
    });
  }

  public retrieveCarrito(carritoId) {
    this.carritoService()
      .find(carritoId)
      .then(res => {
        this.carrito = res;
      })
      .catch(error => {
        this.alertService().showHttpError(this, error.response);
      });
  }

  public previousState() {
    this.$router.go(-1);
  }
}
