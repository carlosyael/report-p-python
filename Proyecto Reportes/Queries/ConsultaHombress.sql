
select nombre, id_usuario from usuarios --oioioioikoi
where Sexo='M'
and case 
        when sexo='M' then 1
        when sexo='F' then 0
    end =1;     
