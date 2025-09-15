document.addEventListener('DOMContentLoaded', function() {
	const form = document.getElementById('notasForm');
	const resultadoDiv = document.getElementById('resultado');

	form.addEventListener('submit', async function(e) {
		e.preventDefault();
		const ap1 = document.getElementById('ap1').value;
		const ap2 = document.getElementById('ap2').value;
		const ac = document.getElementById('ac').value;

		try {
			const response = await fetch('http://127.0.0.1:5000/calcular', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({ ap1, ap2, ac })
			});
			const data = await response.json();
			resultadoDiv.textContent = data.resultado;
		} catch (error) {
			resultadoDiv.textContent = 'Erro ao conectar com o servidor.';
		}
	});
});
