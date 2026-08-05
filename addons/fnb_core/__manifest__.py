{
    "name": "F&B Core",
    "summary": "Core master data and approval workflows for the F&B ERP portfolio project",
    "version": "18.0.1.1.0",
    "category": "Operations/Inventory",
    "license": "LGPL-3",
    "author": "Kim Thu",
    "depends": ["base", "product", "stock", "purchase"],
    "data": [
        "security/fnb_security.xml",
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/purchase_order_views.xml",
    ],
    "installable": True,
    "application": False,
}
