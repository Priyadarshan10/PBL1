document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("upload-form");
  const summaryOutput = document.getElementById("summary-output");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    summaryOutput.innerHTML = "<p>⏳ Generating summary...</p>";

    const formData = new FormData(form);

    try {
      const response = await fetch("http://localhost:5000/summarize", {
        method: "POST",
        body: formData
      });

      const data = await response.json();

      if (response.ok) {
        if (data.summary && data.summary.length) {
          summaryOutput.innerHTML = `<h2>✅ Summary:</h2><ul>` +
            data.summary.map((line, i) => `<li>${i + 1}. ${line}</li>`).join("") +
            `</ul>`;

          // Create a download link
          const downloadLink = document.createElement("a");
          const summaryText = data.summary.map(line => `- ${line}`).join("\n");
          const blob = new Blob([summaryText], { type: "text/plain" });
          const url = URL.createObjectURL(blob);

          downloadLink.href = url;
          downloadLink.download = "summary.txt";
          downloadLink.textContent = "📥 Download Summary";
          downloadLink.className = "download-button";

          summaryOutput.appendChild(downloadLink);
        } else {
          summaryOutput.innerHTML = "<p>⚠️ No relevant sentences found with the given keywords.</p>";
        }
      } else {
        summaryOutput.innerHTML = `<p>❌ Error: ${data.error}</p>`;
      }
    } catch (error) {
      console.error("Error:", error);
      summaryOutput.innerHTML = "<p>❌ Failed to fetch summary. Is the backend running?</p>";
    }
  });
});
