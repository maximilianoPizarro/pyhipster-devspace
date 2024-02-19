import { IProductoCategoria } from '@/shared/model/producto-categoria.model';
import { IProductoOrden } from '@/shared/model/producto-orden.model';

import { Medida } from '@/shared/model/enumerations/medida.model';
export interface IProducto {
  id?: number;
  nombre?: string;
  description?: string | null;
  medida?: Medida;
  imageContentType?: string | null;
  image?: string | null;
  productoCategoria?: IProductoCategoria;
  productoOrdens?: IProductoOrden[] | null;
}

export class Producto implements IProducto {
  constructor(
    public id?: number,
    public nombre?: string,
    public description?: string | null,
    public medida?: Medida,
    public imageContentType?: string | null,
    public image?: string | null,
    public productoCategoria?: IProductoCategoria,
    public productoOrdens?: IProductoOrden[] | null
  ) {}
}
