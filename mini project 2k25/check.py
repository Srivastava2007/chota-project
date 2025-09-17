async function analyzeRisk() {
    const form = document.getElementById('riskForm');
    const results = {
        total: 0,
        categoryScores: {}
    };
    
    // Calculate scores
    for (let i = 1; i <= 6; i++) {
        const value = parseInt(form.elements[i-1].value);
        const score = questionValues[i][value];
        results.total += score;
        results.categoryScores[i] = score;
    }
    
    // Calculate percentage (max possible score is 270)
    const riskPercent = Math.round((results.total / 270) * 100);
    
    // Save to backend
    try {
        const response = await fetch('http://localhost:5000/api/risk-assessment', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                answers: {
                    accountCount: form.elements[0].value,
                    passwordReuse: form.elements[1].value,
                    twoFactorAuth: form.elements[2].value,
                    infoSharing: form.elements[3].value,
                    appPermissions: form.elements[4].value,
                    pastBreaches: form.elements[5].value,
                },
                totalScore: results.total,
                categoryScores: results.categoryScores,
                riskPercent: riskPercent
            })
        });
        if (!response.ok) throw new Error('Failed to save data');
    } catch (error) {
        console.error('Error saving risk assessment:', error);
    }
    
    displayResults(results, riskPercent);
}
