function updateVisitorCounter() {
  fetch('https://r4cs6thxoa.execute-api.us-east-1.amazonaws.com/prd')
      .then(response => response.json())
      .then(data => {
          if (data.statusCode === 200) {
              const newCount = data.body.new_count;
              document.getElementById('visitor-counter').innerText = newCount;
          } else {
              console.error('Failed to update visitor count:', data.body.message);
          }
      })
      .catch(error => {
          console.error('Error fetching visitor count:', error);
      });
}

updateVisitorCounter();