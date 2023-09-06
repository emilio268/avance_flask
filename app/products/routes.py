from flask import render_template
from . import products
from .forms import NewProductForm
import app
import os #manipulación de carpetas 

@products.route('/create',
                methods=["GET" , "POST"])
def crear_producto():
    p = app.models.Producto()                                                                                          
    form = NewProductForm()
    if form.validate_on_submit():
        #llenar atributos 
        #del objeto producto 
        #con el frmularoio 
        form.populate_obj(p)
        #registrar producto en base de datos
        app.db.session.add(p)
        p.imagen = form.imagen.data.filename
        app.db.session.commit()
        
        
        #Transladar la imagen cagada a la carpeta 
        #app/productos/imagenes
        archivo = form.imagen.data
        archivo.save( os.path.abspath( os.getcwd () +'/app/products/imagenes/'+ p.imagen) )
        return os.getcwd()
    return render_template('new.html', form = form)