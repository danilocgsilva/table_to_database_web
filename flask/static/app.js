const dropzone = document.getElementById('dropzone');
const input = document.getElementById('file');
const info = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const clearBtn = document.getElementById('clearBtn');

function formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

function showFileDetails(file) {
    if (!file) return;
    fileName.textContent = file.name;
    fileSize.textContent = formatBytes(file.size);
    info.classList.remove('hidden');
}

['dragenter', 'dragover'].forEach(evt => {
    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add('drag-active');
    });
});

;['dragleave', 'drop'].forEach(evt => {
    dropzone.addEventListener(evt, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('drag-active');
    });
});

dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files && files[0]) {
        input.files = files;
        showFileDetails(files[0]);
    }
});

input.addEventListener('change', (e) => {
    const file = e.target.files[0];
    showFileDetails(file);
});

clearBtn.addEventListener('click', () => {
    input.value = '';
    info.classList.add('hidden');
    fileName.textContent = '';
    fileSize.textContent = '';
});