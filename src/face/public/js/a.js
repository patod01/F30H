async function ejecuta(accion) {
     const api = `${window.api_link}/ejecuta/${accion}`;
     const options = {
          method: `GET`,
          headers: {'Content-Type': 'application/json'},
     };
     return await fetch(`${api}`, options)
          .then(response => response.json());
}
