function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' })) // Gère la résolution
    .catch(() => new Error()) // Gère le rejet
    .finally(() => console.log('Got a response from the API')); // Log universel
}

export default handleResponseFromAPI;
