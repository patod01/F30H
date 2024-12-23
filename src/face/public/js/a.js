async function ejecuta(accion) {
     const api = `${window.api_link}/ejecuta/${accion}`;
     const options = {
          method: `GET`,
          headers: {'Content-Type': 'application/json'},
     };
     return await fetch(`${api}`, options)
          .then(response => response.json());
}

async function ejecutar(accion, info) {
     const api = `${window.api_link}/${accion}`;
     const options = {
          method: `POST`,
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(info)
     };
     return await fetch(`${api}`, options)
          .then(response => response.json());
}
