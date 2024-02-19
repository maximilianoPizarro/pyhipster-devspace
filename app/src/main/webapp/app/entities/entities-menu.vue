<template>
  <div>
    <b-dropdown-item to="/producto">
      <font-awesome-icon icon="asterisk" />
      <span v-text="$t('global.menu.entities.producto')">Producto</span>
    </b-dropdown-item>
    <b-dropdown-item to="/producto-categoria">
      <font-awesome-icon icon="asterisk" />
      <span v-text="$t('global.menu.entities.productoCategoria')">Producto Categoria</span>
    </b-dropdown-item>
    <b-dropdown-item to="/cliente">
      <font-awesome-icon icon="asterisk" />
      <span v-text="$t('global.menu.entities.cliente')">Cliente</span>
    </b-dropdown-item>
    <b-dropdown-item to="/carrito">
      <font-awesome-icon icon="asterisk" />
      <span v-text="$t('global.menu.entities.carrito')">Carrito</span>
    </b-dropdown-item>
    <b-dropdown-item to="/producto-orden">
      <font-awesome-icon icon="asterisk" />
      <span v-text="$t('global.menu.entities.productoOrden')">Producto Orden</span>
    </b-dropdown-item>
    <!-- jhipster-needle-add-entity-to-menu - JHipster will add entities to the menu here -->
  </div>
</template>

<script lang="ts" src="./entities-menu.component.ts"></script>
