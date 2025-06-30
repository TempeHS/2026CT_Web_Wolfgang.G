
function toggleTheme() {
  const body = document.getElementById('theme');
  const cards = document.querySelectorAll('.card'); 
  const slider = document.getElementById('carousel slide'); 
  const sliderItems = document.querySelectorAll('.carousel-item'); 
  const navbar = document.getElementById('navbar'); 
  const dropdownMenu = document.getElementById('dropdownMenu');

  if (body.classList.contains('bg-light')) {
  
    body.classList.remove('bg-light', 'text-dark');
    body.classList.add('bg-dark', 'text-light');


    cards.forEach(card => {
      card.classList.add('bg-dark', 'text-light');
    });

    
    if (slider) {
      slider.classList.add('bg-dark');
    }
    sliderItems.forEach(item => {
      item.classList.add('bg-dark');
    });

  
    if (navbar) {
      navbar.classList.remove('navbar-light', 'bg-light');
      navbar.classList.add('navbar-dark', 'bg-dark');
    }

    if (dropdownMenu) {
      dropdownMenu.classList.add('dropdown-menu-dark');
    }
    
    localStorage.setItem('theme', 'dark');
  } else {
  
    body.classList.remove('bg-dark', 'text-light');
    body.classList.add('bg-light', 'text-dark');

  
    cards.forEach(card => {
      card.classList.remove('bg-dark', 'text-light');
    });

  
    if (slider) {
      slider.classList.remove('bg-dark');
    }
    sliderItems.forEach(item => {
      item.classList.remove('bg-dark');
    });

    
    if (navbar) {
      navbar.classList.remove('navbar-dark', 'bg-dark');
      navbar.classList.add('navbar-light', 'bg-light');
    }


    if (dropdownMenu) {
      dropdownMenu.classList.remove('dropdown-menu-dark');
    }

    localStorage.setItem('theme', 'light');
  }
}


function applySavedTheme() {
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    const body = document.getElementById('theme');
    const cards = document.querySelectorAll('.card'); 
    const slider = document.getElementById('carousel'); 
    const sliderItems = document.querySelectorAll('.carousel-item'); 
    const navbar = document.getElementById('navbar'); 


    body.classList.remove('bg-light', 'text-dark');
    body.classList.add('bg-dark', 'text-light');


    cards.forEach(card => {
      card.classList.add('bg-dark', 'text-light');
    });

  
    if (slider) {
      slider.classList.add('bg-dark');
    }
    sliderItems.forEach(item => {
      item.classList.add('bg-dark');
    });


    if (navbar) {
      navbar.classList.remove('navbar-light', 'bg-light');
      navbar.classList.add('navbar-dark', 'bg-dark');
    }
  }
}


document.addEventListener('DOMContentLoaded', applySavedTheme);