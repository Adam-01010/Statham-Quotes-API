async function getQuote(){
    try{
        const response = await fetch('/quote');
        const data = await response.json();
        document.getElementById('quote').textContent = data.quote;
    } catch (error) {
        console.error('Ошибка при получении цитаты:', error);
    }
}

async function sendMyQuote(){
    myQuote = document.getElementById('myQuote').value;
    try{
        if (!myQuote.trim()) {
            alert("Пожалуйста, введите цитату перед сохранением.");
            return;
        }
        response = await fetch('/add_quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                quote: myQuote
            })
        });
        document.getElementById('myQuote').value = '';
        const data = await response.json();
        alert(data.message + "\n" + data.quote, "Ваша цитата сохранена!");
    }
    catch (error) {
        console.error('Ошибка при отправке цитать:', error);
    }
}