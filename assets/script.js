async function downloadFile() {
    let result = await window.pywebview.api.download_text();
    alert(result);
}