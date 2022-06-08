/*Consultar las temperaturas de un usuario donde las temperaturas se encuentren entre los 25 y 27 grados*/
SELECT COUNT(USER_NAME)AS PETICIONES,USER_NAME FROM FORECAST WHERE TEMP >= 25 and TEMP <= 27 
	GROUP BY USER_NAME
	ORDER BY PETICIONES DESC
	LIMIT 1;
/*Listar los lugares con sus temperaturas mínima y máxima registrada*/
SELECT LOCATION, MAX(TEMP),MIN(TEMP) FROM FORECAST WHERE LOCATION != "" GROUP BY LOCATION;

/*Obtener los lugares con mas o igual a 3 consultas*/
SELECT * FROM (SELECT COUNT(LOCATION)AS PETICIONES,LOCATION FROM FORECAST GROUP BY LOCATION)
	WHERE PETICIONES >= 3
	ORDER BY PETICIONES ASC;

/*Cantidad de veces que los usuarios buscaron un lugar*/
SELECT USER_NAME,LOCATION,COUNT(LOCATION) FROM FORECAST 
	WHERE USER_NAME != "" 
	GROUP BY USER_NAME,LOCATION;

/*Número de consultas realizadas por cada usuario en los últimos 5 días*/
SELECT USER_NAME,COUNT(LOCATION) FROM FORECAST 
	WHERE USER_NAME != "" 
		AND `DATE` BETWEEN DATE('NOW', '-5 day') 
		AND DATE('NOW') GROUP BY USER_NAME;