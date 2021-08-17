function updateOptions(options) {
  const update = { ...options };

  update.headers = { "X-CSRFToken": "" };

  return update;
}
export function fetcher(url, options) {
  return fetch(url, updateOptions(options));
}
