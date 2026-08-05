FROM odoo:18.0

USER root

COPY --chown=odoo:odoo addons /mnt/extra-addons

RUN find /mnt/extra-addons -type f -name '*.py' -exec chmod 0644 {} \; \
    && find /mnt/extra-addons -type d -exec chmod 0755 {} \;

USER odoo

ENV ODOO_RC=/etc/odoo/odoo.conf
