function onResponsiveMenu() {
  const menuBtn = document.getElementById('menuBtn');
  const closeBtn = document.getElementById('closeBtn');
  const sidebar = document.getElementById('sidebar');
  menuBtn?.addEventListener('click', () => {
    sidebar.classList.remove('-translate-x-full');
  });
  closeBtn?.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
  });
}

onResponsiveMenu();
