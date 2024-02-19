/* tslint:disable max-line-length */
import { shallowMount, createLocalVue, Wrapper } from '@vue/test-utils';
import sinon, { SinonStubbedInstance } from 'sinon';
import { ToastPlugin } from 'bootstrap-vue';

import * as config from '@/shared/config/config';
import ProductoOrdenComponent from '@/entities/producto-orden/producto-orden.vue';
import ProductoOrdenClass from '@/entities/producto-orden/producto-orden.component';
import ProductoOrdenService from '@/entities/producto-orden/producto-orden.service';
import AlertService from '@/shared/alert/alert.service';

const localVue = createLocalVue();
localVue.use(ToastPlugin);

config.initVueApp(localVue);
const i18n = config.initI18N(localVue);
const store = config.initVueXStore(localVue);
localVue.component('font-awesome-icon', {});
localVue.component('b-badge', {});
localVue.directive('b-modal', {});
localVue.component('b-button', {});
localVue.component('router-link', {});

const bModalStub = {
  render: () => {},
  methods: {
    hide: () => {},
    show: () => {},
  },
};

describe('Component Tests', () => {
  describe('ProductoOrden Management Component', () => {
    let wrapper: Wrapper<ProductoOrdenClass>;
    let comp: ProductoOrdenClass;
    let productoOrdenServiceStub: SinonStubbedInstance<ProductoOrdenService>;

    beforeEach(() => {
      productoOrdenServiceStub = sinon.createStubInstance<ProductoOrdenService>(ProductoOrdenService);
      productoOrdenServiceStub.retrieve.resolves({ headers: {} });

      wrapper = shallowMount<ProductoOrdenClass>(ProductoOrdenComponent, {
        store,
        i18n,
        localVue,
        stubs: { bModal: bModalStub as any },
        provide: {
          productoOrdenService: () => productoOrdenServiceStub,
          alertService: () => new AlertService(),
        },
      });
      comp = wrapper.vm;
    });

    it('Should call load all on init', async () => {
      // GIVEN
      productoOrdenServiceStub.retrieve.resolves({ headers: {}, data: [{ id: 123 }] });

      // WHEN
      comp.retrieveAllProductoOrdens();
      await comp.$nextTick();

      // THEN
      expect(productoOrdenServiceStub.retrieve.called).toBeTruthy();
      expect(comp.productoOrdens[0]).toEqual(expect.objectContaining({ id: 123 }));
    });
    it('Should call delete service on confirmDelete', async () => {
      // GIVEN
      productoOrdenServiceStub.delete.resolves({});

      // WHEN
      comp.prepareRemove({ id: 123 });
      expect(productoOrdenServiceStub.retrieve.callCount).toEqual(1);

      comp.removeProductoOrden();
      await comp.$nextTick();

      // THEN
      expect(productoOrdenServiceStub.delete.called).toBeTruthy();
      expect(productoOrdenServiceStub.retrieve.callCount).toEqual(2);
    });
  });
});
