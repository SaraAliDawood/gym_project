{
    "name": "Gym Project",
    "version": "1.0",
    "sequence": 1,
    "summary": "Gym Appointments & Subscriptions",
    "author": "sara dawood",
    "depends": ["base", "product", "web"],
 "data": [
    "security/ir.model.access.csv",
    "views/gym_appointment_view.xml",
    "views/gym_trainer_view.xml",
    "views/gym_trainee_view.xml",
    "views/product_views.xml",
    "views/menu.xml",
    "reports/trainer_report.xml",
    "reports/gym_subscription_report.xml",
    "views/wizard_views.xml",
    "views/gym_subscription_view.xml"
],

    'assets': {
    'web.assets_backend': [
        'gym_project/static/src/js/youtube.js',
        'gym_project/static/src/xml/youtube.xml',
    ],
},

    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
