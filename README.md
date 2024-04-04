# Instalacion

1. Clonar repositorio

```bash
git clone https://github.com/b-munar/partner
```

2. Copiar el .env.template y pegarlo en un .env

3. 

```bash
docker compose build
docker compose up
```


El servicio de orchestrator consume el servicio auth, sportmen y subscription. Este servicio ahorra el trabajo de hacer register/login en auth, register/get en sportman y get en subscription.

## 2. Register Partner

Crea un usuario sportment con los datos brindados, el email del usuario debe ser único.

<table>
<tr>
<td> Método </td>
<td> POST </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6650/partner</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>N/A</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>

```json
{
  "user": "28a3ad77-7d3c-47e3-9c42-858ca3ec5222",
  "name": "parnert",
  "last_name": "parnert",
  "age": 20,
  "profession": "cowboy",
  "license": "Hunter X",
  "country_birth": "Colombia",
  "city_birth": "Cali",
  "country_residence": "Colombia",
  "city_residence": "Elvira",
  "sports": ["basketball"],
  "companies": ["Uniandes"],
  "type_services": ["education"]
 
}
```
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 201 </td>
<td>En el caso que el usuario se haya creado con éxito.</td>
<td>

```json
{
  "partner": {
    "name": "parnert",
    "last_name": "parnert",
    "age": 20,
    "profession": "cowboy",
    "license": "Hunter X",
    "country_birth": "Colombia",
    "city_birth": "Cali",
    "country_residence": "Colombia",
    "city_residence": "Elvira",
    "sports": [
      "basketball"
    ],
    "companies": [
      "Uniandes"
    ],
    "type_services": [
      "education"
    ],
    "created_at": "2024-04-04T04:33:43"
  }
}
```
</td>
</tr>
</tbody>
</table>


## 2. Obtener Partner

Obtener Deportista
<table>
<tr>
<td> Método </td>
<td> GET </td>
</tr>
<tr>
<td> Ruta </td>
<td> <strong>localhost:6650/partner</strong> </td>
</tr>
<tr>
<td> Parámetros </td>
<td> N/A </td>
</tr>
<tr>
<td> Encabezados </td>
<td>
 "Authorization": "Bearer eyJ0eXAiOiJKV1QiL..."
</td>
</tr>
<tr>
<td> Cuerpo </td>
<td>
N/A
</td>
</tr>
</table>

### Respuestas

<table>
<tr>
<th> Código </th>
<th> Descripción </th>
<th> Cuerpo </th>
</tr>
<tbody>
<td> 200 </td>
<td>En el caso de exito.</td>
<td>

```json
{
  "partner": {
    "name": "parnert",
    "last_name": "parnert",
    "age": 20,
    "profession": "cowboy",
    "license": "Hunter X",
    "country_birth": "Colombia",
    "city_birth": "Cali",
    "country_residence": "Colombia",
    "city_residence": "Elvira",
    "sports": [
      "basketball"
    ],
    "companies": [
      "Uniandes"
    ],
    "type_services": [
      "education"
    ],
    "created_at": "2024-04-04T18:53:56"
  }
}
```
</td>
