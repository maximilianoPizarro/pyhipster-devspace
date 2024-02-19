import { Component, Provide, Vue } from 'vue-property-decorator';

import UserService from '@/entities/user/user.service';
import ProductoService from './producto/producto.service';
import ProductoCategoriaService from './producto-categoria/producto-categoria.service';
import ClienteService from './cliente/cliente.service';
import CarritoService from './carrito/carrito.service';
import ProductoOrdenService from './producto-orden/producto-orden.service';
// jhipster-needle-add-entity-service-to-entities-component-import - JHipster will import entities services here

@Component
export default class Entities extends Vue {
  @Provide('userService') private userService = () => new UserService();
  @Provide('productoService') private productoService = () => new ProductoService();
  @Provide('productoCategoriaService') private productoCategoriaService = () => new ProductoCategoriaService();
  @Provide('clienteService') private clienteService = () => new ClienteService();
  @Provide('carritoService') private carritoService = () => new CarritoService();
  @Provide('productoOrdenService') private productoOrdenService = () => new ProductoOrdenService();
  // jhipster-needle-add-entity-service-to-entities-component - JHipster will import entities services here
}
