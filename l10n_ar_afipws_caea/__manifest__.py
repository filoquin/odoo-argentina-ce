{
    'name': "Factura Electrónica Argentina CAEA",

    'summary': """
        Habilit< la gestion de CAEA""",
    'sequence': 14,

    'description': """
         Permita consignar en los comprobantes respaldatorios de las operaciones,
          el Código de Autorización Electrónico Anticipado "CAEA", en reemplazo del "CAE"  
          http://www.afip.gov.ar/genericos/guiavirtual/directorio_subcategoria_nivel3.aspx?id_nivel1=562id_nivel2=603&id_nivel3=1663   
          Requisitos
          http://www.afip.gov.ar/genericos/guiavirtual/consultas_detalle.aspx?id=13872311
          c) Posean un sistema logístico integrado de almacenes, "stock", comercialización, facturación y distribución de tal magnitud que dificulte la facturación electrónica bajo la modalidad de Código de Autorización Electrónico "CAE". A fin de analizar el cumplimiento de la presente condición, no podrán considerarse las operaciones con consumidores finales.
          d) Hayan emitido en cada mes calendario un mínimo de 1.800 comprobantes (Facturas, recibos, notas de crédito y notas de débito clases "A", "A" con leyenda "PAGO EN CBU INFORMADA", "M", "B" y "C"), en el período de 3 meses calendarios inmediatos anteriores a la solicitud de incorporación al procedimiento especial. No podrán considerarse para el cumplimiento de la mencionada condición los comprobantes por operaciones con consumidores finales

            13874653 - Evento 2779 - ¿Cómo se realiza la solicitud de adhesión al régimen?
            La solicitud de adhesión deberá realizarse ingresando al servicio con clave fiscal "Regímenes de Facturación y Registración (REAR/RECE/RFI)". Asimismo, se deberá comunicar el período a partir del cual comenzará a aplicar el procedimiento especial y si la adhesión se efectúa bajo la modalidad de emisión complementaria a la principal - contingencia - (p.ej. Controlador Fiscal, Factura Electrónica) conforme lo previsto en el Título III RG 4290/18.

        Como constancia de la presentación realizada y admitida, el sistema emitirá un comprobante que tendrá el carácter de acuse de recibo.

Evento 2785 - ¿Se debe habilitar un nuevo punto de venta para el CAEA?
Para los comprobantes que se emitan bajo la modalidad excepcional complementaria a la principal (contingencia) conforme a lo previsto en el Título III RG 4290/18, se deberán habilitar puntos de venta específicos por dicha modalidad asociados al mismo domicilio de la modalidad de emisión principal y a su condición ante el impuesto al valor agregado.
¿Cómo debo proceder en caso de no haber solicitado el CAEA durante una quincena?
09/06/2015 12:00:00 a.m.

De acuerdo al artículo primero de la RG 2926, el CAEA es un procedimiento opcional en reemplazo del CAE.

Según lo expuesto, si el contribuyente es un obligado a Factura Electrónica y no puede realizar los comprobantes con CAEA deberán ser generados con CAE. Al no haber solicitado CAEA, no deben informar nada para esa quincena. 
¿Hay un límite en la cantidad de comprobantes a emitir por medios alternativos de contingencia?
28/08/2018 12:00:00 a.m.

Las modalidades alternativas ante inconvenientes con el uso del controlador fiscal o de la emisión de comprobantes electrónicos, sólo deben ser utilizadas en condiciones de excepcionalidad.

Se considera que no se cumple con la condición de excepcionalidad cuando, durante 2 meses consecutivos o 3 meses alternados en un año calendario, se observe alguna de las siguientes irregularidades:

a) que la emisión de comprobantes con CAEA o CAI excedan significativamente el nivel de facturación regular, es decir la cantidad de comprobantes emitidos mensualmente por excepción representan un 5%, o más, respecto del total de la sucursal.

b) La contingencia con CAEA, como alternativa de la emisión de comprobantes electrónicos, medida en tiempo, no deberá superar el 5% del lapso total de disponibilidad de servicios ofrecidos por AFIP en forma mensual, medido por sucursal.

A fin de determinar la condición de excepcionalidad, no serán consideradas las causas que se originan en inconvenientes en la disponibilidad de los servicios de comunicación atribuibles a este Organismo.

          """,
    'author': "Filoquin",
    'website': "http://www.sipecu.com.ar",

    'category': 'Localization/Argentina',
    'version': '13.0.1.0.0',
    'depends': ['l10n_ar_afipws_fe'],

    'data': [
        'security/ir.model.access.csv',
        'views/account_journal.xml',
        'views/afipws_caea.xml',
        'views/company.xml',
        'views/res_config_settings.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}
