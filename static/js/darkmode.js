function toggleTheme() {
  const body = document.getElementById('theme');
  const cards = document.querySelectorAll('.card'); 
  const slider = document.getElementById('carouselExampleAutoplaying'); 
  if (body.classList.contains('bg-light')) {

    body.classList.remove('bg-light', 'text-dark');
    body.classList.add('bg-dark', 'text-light');

    cards.forEach(card => {
      card.classList.add('bg-dark', 'text-light');
    });

    if (slider) {
      slider.classList.add('bg-dark');
    }
  } else {
    body.classList.remove('bg-dark', 'text-light');
    body.classList.add('bg-light', 'text-dark');

    cards.forEach(card => {
      card.classList.remove('bg-dark', 'text-light');
    });

    if (slider) {
      slider.classList.remove('bg-dark');
    }
  }
}