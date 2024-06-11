SELECT
    "A1"."ID_USUARIO_0"             "ID_USUARIO",
    "A1"."NOMBRE_1"                 "NOMBRE",
    "A1"."APELLIDO_2"               "APELLIDO",
    "A1"."CORREO_3"                 "CORREO",
    "A1"."SEXO_4"                   "SEXO",
    "A1"."DIRECCION_5"              "DIRECCION",
    "A1"."QCSJ_C000000000300000_6"  "QCSJ_C000000000300000",
    "A1"."TELEFONO_7"               "TELEFONO",
    "A1"."QCSJ_C000000000500000_8"  "QCSJ_C000000000500000",
    "A1"."QCSJ_C000000000300001_9"  "QCSJ_C000000000300001",
    "A1"."PUESTO_10"                "PUESTO",
    "A1"."QCSJ_C000000000500001_11" "QCSJ_C000000000500001",
    "A1"."DEPARTAMENTO_12"          "DEPARTAMENTO"
FROM
    (
        SELECT
            "A3"."ID_USUARIO_0"            "ID_USUARIO_0",
            "A3"."NOMBRE_1"                "NOMBRE_1",
            "A3"."APELLIDO_2"              "APELLIDO_2",
            "A3"."CORREO_3"                "CORREO_3",
            "A3"."SEXO_4"                  "SEXO_4",
            "A3"."DIRECCION_5"             "DIRECCION_5",
            "A3"."QCSJ_C000000000300000_6" "QCSJ_C000000000300000_6",
            "A3"."TELEFONO_7"              "TELEFONO_7",
            "A3"."ID_DEPARTAMENTO_8"       "QCSJ_C000000000500000_8",
            "A3"."QCSJ_C000000000300001_9" "QCSJ_C000000000300001_9",
            "A3"."PUESTO_10"               "PUESTO_10",
            "A2"."ID_DEPARTAMENTO"         "QCSJ_C000000000500001_11",
            "A2"."DEPARTAMENTO"            "DEPARTAMENTO_12"
        FROM
            (
                SELECT
                    "A5"."ID_USUARIO"      "ID_USUARIO_0",
                    "A5"."NOMBRE"          "NOMBRE_1",
                    "A5"."APELLIDO"        "APELLIDO_2",
                    "A5"."CORREO"          "CORREO_3",
                    "A5"."SEXO"            "SEXO_4",
                    "A5"."DIRECCION"       "DIRECCION_5",
                    "A5"."ID_PUESTO"       "QCSJ_C000000000300000_6",
                    "A5"."TELEFONO"        "TELEFONO_7",
                    "A5"."ID_DEPARTAMENTO" "ID_DEPARTAMENTO_8",
                    "A4"."ID_PUESTO"       "QCSJ_C000000000300001_9",
                    "A4"."PUESTO"          "PUESTO_10"
                FROM
                    "SYSTEM"."USUARIOS" "A5",
                    "SYSTEM"."PUESTOS"  "A4"
                WHERE
                    "A5"."ID_PUESTO" = "A4"."ID_PUESTO"
            )                        "A3",
            "SYSTEM"."DEPARTAMENTOS" "A2"
        WHERE
            "A3"."ID_DEPARTAMENTO_8" = "A2"."ID_DEPARTAMENTO"
    ) "A1";

