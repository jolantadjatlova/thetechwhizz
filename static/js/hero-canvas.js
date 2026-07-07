// ===== TECH WHIZZ - HERO CONSTELLATION ANIMATION =====

var canvas = document.getElementById('hero-canvas'),
    can_w = parseInt(canvas.getAttribute('width')),
    can_h = parseInt(canvas.getAttribute('height')),
    ctx = canvas.getContext('2d');

var BALL_NUM = 40;

var ball_color = {
    r: 51,
    g: 194,
    b: 224
};

var R = 2,
    balls = [],
    alpha_f = 0.03,
    link_line_width = 0.8,
    dis_limit = 260,
    mouse_in = false,
    mouse_ball = {
        x: 0,
        y: 0,
        vx: 0,
        vy: 0,
        r: 0,
        type: 'mouse'
    };

function getRandomSpeed(pos) {
    var min = -1, max = 1;
    switch (pos) {
        case 'top': return [randomNumFrom(min, max), randomNumFrom(0.1, max)];
        case 'right': return [randomNumFrom(min, -0.1), randomNumFrom(min, max)];
        case 'bottom': return [randomNumFrom(min, max), randomNumFrom(min, -0.1)];
        case 'left': return [randomNumFrom(0.1, max), randomNumFrom(min, max)];
        default: return;
    }
}

function randomArrayItem(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function randomNumFrom(min, max) {
    return Math.random() * (max - min) + min;
}

function randomSidePos(length) {
    return Math.ceil(Math.random() * length);
}

function getRandomBall() {
    var pos = randomArrayItem(['top', 'right', 'bottom', 'left']);
    switch (pos) {
        case 'top':
            return { x: randomSidePos(can_w), y: -R, vx: getRandomSpeed('top')[0], vy: getRandomSpeed('top')[1], r: R, alpha: 1, phase: randomNumFrom(0, 10) };
        case 'right':
            return { x: can_w + R, y: randomSidePos(can_h), vx: getRandomSpeed('right')[0], vy: getRandomSpeed('right')[1], r: R, alpha: 1, phase: randomNumFrom(0, 10) };
        case 'bottom':
            return { x: randomSidePos(can_w), y: can_h + R, vx: getRandomSpeed('bottom')[0], vy: getRandomSpeed('bottom')[1], r: R, alpha: 1, phase: randomNumFrom(0, 10) };
        case 'left':
            return { x: -R, y: randomSidePos(can_h), vx: getRandomSpeed('left')[0], vy: getRandomSpeed('left')[1], r: R, alpha: 1, phase: randomNumFrom(0, 10) };
    }
}

function renderBalls() {
    balls.forEach(function (b) {
        if (!b.hasOwnProperty('type')) {
            ctx.fillStyle = 'rgba(' + ball_color.r + ',' + ball_color.g + ',' + ball_color.b + ',' + b.alpha + ')';
            ctx.beginPath();
            ctx.arc(b.x, b.y, R, 0, Math.PI * 2, true);
            ctx.closePath();
            ctx.fill();
        }
    });
}

function updateBalls() {
    var new_balls = [];
    balls.forEach(function (b) {
        b.x += b.vx;
        b.y += b.vy;
        if (b.x > -50 && b.x < (can_w + 50) && b.y > -50 && b.y < (can_h + 50)) {
            new_balls.push(b);
        }
        b.phase += alpha_f;
        b.alpha = Math.abs(Math.cos(b.phase));
    });
    balls = new_balls.slice(0);
}

function renderLines() {
    var fraction, alpha;
    for (var i = 0; i < balls.length; i++) {
        for (var j = i + 1; j < balls.length; j++) {
            fraction = getDisOf(balls[i], balls[j]) / dis_limit;
            if (fraction < 1) {
                alpha = (1 - fraction).toString();
                ctx.strokeStyle = 'rgba(51,194,224,' + alpha + ')';
                ctx.lineWidth = link_line_width;
                ctx.beginPath();
                ctx.moveTo(balls[i].x, balls[i].y);
                ctx.lineTo(balls[j].x, balls[j].y);
                ctx.stroke();
                ctx.closePath();
            }
        }
    }
}

function getDisOf(b1, b2) {
    var delta_x = Math.abs(b1.x - b2.x),
        delta_y = Math.abs(b1.y - b2.y);
    return Math.sqrt(delta_x * delta_x + delta_y * delta_y);
}

function addBallIfy() {
    if (balls.length < BALL_NUM) {
        balls.push(getRandomBall());
    }
}

function render() {
    ctx.clearRect(0, 0, can_w, can_h);
    renderBalls();
    renderLines();
    updateBalls();
    addBallIfy();
    window.requestAnimationFrame(render);
}

function initBalls(num) {
    for (var i = 1; i <= num; i++) {
        balls.push({
            x: randomSidePos(can_w),
            y: randomSidePos(can_h),
            vx: getRandomSpeed('top')[0],
            vy: getRandomSpeed('top')[1],
            r: R,
            alpha: 1,
            phase: randomNumFrom(0, 10)
        });
    }
}

function initCanvas() {
    var hero = document.getElementById('hero-canvas');
    var container = hero.parentElement;
    canvas.setAttribute('width', container.offsetWidth);
    canvas.setAttribute('height', container.offsetHeight);
    can_w = parseInt(canvas.getAttribute('width'));
    can_h = parseInt(canvas.getAttribute('height'));
}

window.addEventListener('resize', function () {
    initCanvas();
});

canvas.addEventListener('mouseenter', function () {
    mouse_in = true;
    balls.push(mouse_ball);
});

canvas.addEventListener('mouseleave', function () {
    mouse_in = false;
    var new_balls = [];
    balls.forEach(function (b) {
        if (!b.hasOwnProperty('type')) new_balls.push(b);
    });
    balls = new_balls.slice(0);
});

canvas.addEventListener('mousemove', function (e) {
    mouse_ball.x = e.pageX;
    mouse_ball.y = e.pageY;
});

function goMovie() {
    initCanvas();
    initBalls(BALL_NUM);
    window.requestAnimationFrame(render);
}

goMovie();