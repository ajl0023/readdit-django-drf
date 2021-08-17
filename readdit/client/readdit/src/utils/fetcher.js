function updateOptions(options) {
  const update = { ...options };

  update.headers = {
    Authorization: `Token ${localStorage.getItem("access_token")}`,
  };

  return update;
}
export function fetcher(url, options) {
  return fetch(url, updateOptions(options));
}
