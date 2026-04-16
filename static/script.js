document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const workflowForm = document.getElementById('workflow-form');
    const loadingSection = document.getElementById('loading');
    const responseContainer = document.getElementById('response-container');
    const aiResponseText = document.getElementById('ai-response-text');
    const emailBadge = document.getElementById('email-badge');
    const workflowStatus = document.getElementById('workflow-status');
    const resetBtn = document.getElementById('reset-btn');
    const historyList = document.getElementById('history-list');

    // Tab Logic
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            
            // Toggle active button
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Toggle active content
            tabContents.forEach(content => {
                if (content.id === `${tabId}-tab`) {
                    content.classList.remove('hidden');
                    if (tabId === 'history') loadHistory();
                } else {
                    content.classList.add('hidden');
                }
            });
        });
    });

    // Form Submission
    workflowForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const query = document.getElementById('query').value.trim();
        const email = document.getElementById('email').value.trim();

        if (!query) return;

        // Toggle UI
        workflowForm.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        responseContainer.classList.add('hidden');

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query, email }),
            });

            const data = await response.json();

            if (response.ok) {
                // Update response UI
                workflowStatus.textContent = data.status;
                aiResponseText.textContent = data.ai_response;
                
                // Email badge logic
                emailBadge.textContent = data.email_status;
                if (data.email_status.includes('successfully') || data.email_status.includes('sent')) {
                    emailBadge.className = 'badge badge-success';
                } else if (data.email_status.includes('failed')) {
                    emailBadge.className = 'badge badge-fail';
                } else {
                    emailBadge.className = 'badge'; // Default
                }

                loadingSection.classList.add('hidden');
                responseContainer.classList.remove('hidden');
            } else {
                throw new Error(data.error || 'Automation failed');
            }

        } catch (error) {
            alert('Workflow Error: ' + error.message);
            loadingSection.classList.add('hidden');
            workflowForm.classList.remove('hidden');
        }
    });

    // Reset Logic
    resetBtn.addEventListener('click', () => {
        workflowForm.reset();
        responseContainer.classList.add('hidden');
        workflowForm.classList.remove('hidden');
    });

    // Fetch History
    async function loadHistory() {
        historyList.innerHTML = '<div class="loader-sm"></div>';
        
        try {
            const response = await fetch('/history');
            const data = await response.json();

            if (data.length === 0) {
                historyList.innerHTML = '<p class="empty-msg">No history records found.</p>';
                return;
            }

            historyList.innerHTML = data.map(item => `
                <div class="history-item">
                    <p class="history-query">Q: ${item.query}</p>
                    <p class="history-response">${item.response}</p>
                    <span class="history-time">${formatDate(item.timestamp)}</span>
                </div>
            `).join('');

        } catch (error) {
            historyList.innerHTML = `<p class="error-msg">Failed to load history: ${error.message}</p>`;
        }
    }

    function formatDate(dateStr) {
        const date = new Date(dateStr);
        return date.toLocaleString();
    }
});
