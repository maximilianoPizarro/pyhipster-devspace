import { Component, Vue, Inject } from 'vue-property-decorator';
import Vue2Filters from 'vue2-filters';
import { IProductoOrden } from '@/shared/model/producto-orden.model';

import ProductoOrdenService from './producto-orden.service';
import AlertService from '@/shared/alert/alert.service';

@Component({
  mixins: [Vue2Filters.mixin],
})
export default class ProductoOrden extends Vue {
  @Inject('productoOrdenService') private productoOrdenService: () => ProductoOrdenService;
  @Inject('alertService') private alertService: () => AlertService;

  private removeId: number = null;

  public productoOrdens: IProductoOrden[] = [];

  public isFetching = false;

  public mounted(): void {
    this.retrieveAllProductoOrdens();
  }

  public clear(): void {
    this.retrieveAllProductoOrdens();
  }

  public retrieveAllProductoOrdens(): void {
    this.isFetching = true;
    this.productoOrdenService()
      .retrieve()
      .then(
        res => {
          this.productoOrdens = res.data;
          this.isFetching = false;
        },
        err => {
          this.isFetching = false;
          this.alertService().showHttpError(this, err.response);
        }
      );
  }

  public handleSyncList(): void {
    this.clear();
  }

  public prepareRemove(instance: IProductoOrden): void {
    this.removeId = instance.id;
    if (<any>this.$refs.removeEntity) {
      (<any>this.$refs.removeEntity).show();
    }
  }

  public removeProductoOrden(): void {
    this.productoOrdenService()
      .delete(this.removeId)
      .then(() => {
        const message = this.$t('deliveryApp.productoOrden.deleted', { param: this.removeId });
        this.$bvToast.toast(message.toString(), {
          toaster: 'b-toaster-top-center',
          title: 'Info',
          variant: 'danger',
          solid: true,
          autoHideDelay: 5000,
        });
        this.removeId = null;
        this.retrieveAllProductoOrdens();
        this.closeDialog();
      })
      .catch(error => {
        this.alertService().showHttpError(this, error.response);
      });
  }

  public closeDialog(): void {
    (<any>this.$refs.removeEntity).hide();
  }
}
