const themeSelector = document.querySelector('#theme-selector')

themeSelector.addEventListener('change', (e) => {
  const selectedTheme = e.target.value;
  document.body.setAttribute('data-theme', selectedTheme);
})

