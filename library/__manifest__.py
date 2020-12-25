{'name': 'Aplicación para la gestión biblioteca',

 'summary': """
        Gestiona y almacena los libros para la empresa slx""",


 'description': 'Library books.',

 'author': 'Matías Monsalve',

 'website': "https://github.com/MNMFgeforce/ProyectoOdoo",

 'category': 'Proyecto desarrollo de aplicaciones Web 2',

    'version': '0.1',

 'depends': ['base'],

 'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/book_view.xml',
    'views/book_category_view.xml',
    'views/book_list_template.xml',
    'reports/library_book_report.xml',
    'reports/library_book_sql_report.xml',
 ],
 'demo': [
    'data/res.partner.csv',
    'data/library.book.csv',
    'data/book_demo.xml',
 ],
 'application': True,
 'installable': True,
}


