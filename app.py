from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Will You Be Mine?</title>
        <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti"></script> <!-- Confetti library -->
        <style>
            /* Global Styling */
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: 'Roboto', sans-serif;
                background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
                color: #ff66b2;
                text-align: center;
                padding: 0;
                margin: 0;
                transition: all 0.3s ease;
            }

            h1 {
                font-family: 'Dancing Script', cursive;
                font-size: 3.5em;
                color: #ff3399;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
                margin-top: 50px;
                opacity: 0;
                animation: fadeIn 1s forwards;
            }

            p {
                font-size: 1.5em;
                color: #ff3399;
                margin-top: 20px;
                font-weight: bold;
                opacity: 0;
                animation: fadeIn 1.5s forwards;
                animation-delay: 0.5s;
            }

            /* Desmos Graph Styling */
            .desmos-iframe-wrapper {
                width: 100%;
                max-width: 700px;
                height: 500px;
                margin: 30px auto;
                display: flex;
                justify-content: center;
                align-items: center;
                border-radius: 20px;
                box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                opacity: 0;
                animation: fadeIn 2s forwards;
                animation-delay: 1s;
                position: relative;
            }

            .desmos-iframe-wrapper:hover {
                transform: scale(1.03);
                box-shadow: 0px 15px 40px rgba(0, 0, 0, 0.2);
            }

            .desmos-iframe {
                width: 100%;
                height: 100%;
                border-radius: 20px;
                border: none;
            }

            /* Hidden Question with Smooth Visibility */
            .answer-box {
                visibility: hidden;
                font-size: 2.5em;
                color: #ff3399;
                font-weight: bold;
                margin-top: 20px;
                transition: visibility 0.3s ease, opacity 0.5s ease;
                opacity: 0;
                text-align: center;
                max-width: 600px;
                margin: 30px auto;
            }

            .answer-box.visible {
                visibility: visible;
                opacity: 1;
            }

            .answer-box input {
                padding: 10px;
                font-size: 1.2em;
                border-radius: 10px;
                border: 2px solid #ff66b2;
                outline: none;
                transition: background-color 0.3s ease;
                margin-top: 10px;
                width: 80%;
            }

            .answer-box input:focus {
                background-color: #fff0f7;
            }

            .answer-box button {
                background-color: #ff66b2;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 10px;
                cursor: pointer;
                margin-left: 10px;
                transition: background-color 0.3s;
                font-size: 1.2em;
            }

            .answer-box button:hover {
                background-color: #ff3399;
            }

            footer {
                position: absolute;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                font-size: 1.2em;
                color: #ff66b2;
                padding: 10px;
                text-align: center;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
                opacity: 0;
                visibility: hidden;
                animation: fadeIn 3s forwards;
                animation-delay: 2s;
            }

            footer a {
                color: #ff66b2;
                text-decoration: none;
                font-weight: bold;
            }

            footer a:hover {
                text-decoration: underline;
            }

            .desmos-iframe-wrapper:hover footer {
                opacity: 1;
                visibility: visible;
            }

            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }

            /* Responsive Design */
            @media (max-width: 768px) {
                h1 {
                    font-size: 2.5em;
                }

                p {
                    font-size: 1.2em;
                }

                .desmos-iframe-wrapper {
                    width: 90%;
                    height: 400px;
                }

                footer p {
                    font-size: 1em;
                }

                .answer-box input {
                    width: 100%;
                }
            }
        </style>
    </head>
    <body>
        <h1>˚ʚ♡ɞ˚ Welcome, Page-Peeker Princess ˚ʚ♡ɞ˚</h1>
        <p>Hover over the heart below for 2 seconds to see my question! 💖</p>

        <!-- Embed the Desmos graph -->
        <div class="desmos-iframe-wrapper">
            <iframe class="desmos-iframe" 
                    src="https://www.desmos.com/calculator/ayfzbzsqs1" 
                    allowfullscreen></iframe>

            <!-- Footer -->
            <footer>
                <p>To be together, or not to be together… What does your heart say? 💖</p>
            </footer>
        </div>

        <!-- Hidden Question -->
        <div class="answer-box" id="answerBox">
            <p>Between the pages of a book,<br>
            Where words and stories intertwine,<br>
            I’d love to share a quiet moment,<br>
            And spend some time with you, divine.</p>
            <p> What do you say? Would you like to be my girlfriend? I think it’d be a chapter worth writing together ⋆˙⟡♡</p>
            <p>Type 'to be together' for Yes, or 'no' for No.</p>
            <input type="text" id="answerInput" placeholder="Type your answer here...">
            <button onclick="submitAnswer()">Submit</button>
        </div>
        
        <p style="font-size: 1.2em; font-weight: bold; color: #ff3399; margin-top: 30px;">Created by Salvador N., with heartfelt dedication to Ariana M.</p>

        <script>
            let timeout;
            const iframeWrapper = document.querySelector('.desmos-iframe-wrapper');
            const answerBox = document.getElementById('answerBox');
            let boxVisible = false;

            iframeWrapper.addEventListener('mouseenter', () => {
                timeout = setTimeout(() => {
                    answerBox.classList.add('visible'); // Smooth transition for showing answer box
                    boxVisible = true;
                }, 2000);
            });

            iframeWrapper.addEventListener('mouseleave', () => {
                clearTimeout(timeout);
                if (!boxVisible) {
                    answerBox.classList.remove('visible'); // Hide answer box if not yet shown
                }
            });

            // Handle the submission of the answer
            function submitAnswer() {
                const answer = document.getElementById('answerInput').value.toLowerCase();
                if (answer === 'to be together') {
                    alert('You said yes! 💖');
                    triggerConfetti();  // Trigger confetti when user submits 'to be together'
                } else if (answer === 'no') {
                    alert('I understand, no worries. 💕');
                } else {
                    alert('Please respond with "to be together" or "no".');
                }
            }

            // Function to trigger confetti with hearts and books
            function triggerConfetti() {
                const duration = 5 * 1000; // Duration of confetti (5 seconds)
                const count = 200; // Number of confetti particles

                const confettiSettings = {
                    particleCount: count,
                    startVelocity: 30,
                    spread: 360,
                    ticks: 60,
                    gravity: 0.5,
                    shapes: ['heart', 'square'], // Add 'square' for the book shape
                    colors: ['#ff3399', '#ff66b2', '#ff9a9e'],
                    origin: {
                        x: Math.random(),
                        y: Math.random(),
                    }
                };

                confetti(confettiSettings);
            }
        </script>
    </body>
    </html>
    '''

    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
