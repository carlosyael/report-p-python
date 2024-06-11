select  
    A.nombre,
    A.puesto,
    A.departamento,
    A.id_puesto,
    A.id_departamento,
    A.id_usuario,
    case
        when A.sexo='M' then 1
        else 0
    end as Hombres,
    case
        when A.sexo='F' then 1
        else 0
    end as Mujeres
    
from(
    select 
        u.id_usuario, 
        u.nombre, 
        u.id_puesto,
        p.puesto, 
        u.departamento,
        u.id_departamento,
        u.sexo
    from (Select
            u.id_usuario, 
            u.nombre, 
            u.id_puesto,
            d.departamento,
            d.id_departamento,
            u.sexo 
            from usuarios u
            inner join departamentos d
            on u.Id_departamento= d.Id_departamento
    ) u
    inner join puestos p 
    on u.id_puesto = p.id_puesto
) A
