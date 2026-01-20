const chatBox = document.getElementById("chat-box");

function addMessage(text, cls) {
    const div = document.createElement("div");
    div.className = `msg ${cls}`;
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendQuestion(text=null) {
    const input = document.getElementById("question");
    const question = text || input.value.trim();
    if (!question) return;

    addMessage(question, "user");
    input.value = "";

    const res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ question })
    });

    const data = await res.json();
    addMessage(data.answer, "bot");
}

document.getElementById("question").addEventListener("keypress", e => {
    if (e.key === "Enter") sendQuestion();
});