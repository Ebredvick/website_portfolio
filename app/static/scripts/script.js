function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}

document.getElementById('toggleButton').addEventListener('click', function() {
  var icon = document.getElementById('icon');
  if (icon.classList.contains('fa-moon')) {
      icon.classList.remove('fa-moon');
      icon.classList.add('fa-sun');
  } else {
      icon.classList.remove('fa-sun');
      icon.classList.add('fa-moon');
  }

  const isDark = document.body.getAttribute('data-theme') === 'dark';
  if (isDark) {
      document.body.removeAttribute('data-theme');
      localStorage.removeItem('theme');
  } else {
      document.body.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
  }
});

