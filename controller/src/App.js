import React, { useEffect } from 'react';
import './App.css';
import _ from 'lodash';
const radius = 150;

function actionRaw(left, right) {
  if (Math.max(left, right) > 100 || Math.min(left, right) < -100) {
    return;
  }
  fetch('http://192.168.1.8:2201/control', {
    method: 'POST',
    mode: 'no-cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'content-type': 'application/json'
    },
    referrerPolicy: 'no-referrer',
    body: JSON.stringify({
      left, right
    })
  })
}

const threshold100 = 0.8;

const action = _.debounce(actionRaw, 100, {
  'maxWait': 200,
  'leading': true,
  'trailing': true
})

function calculateMove(event) {
  const centerX = event.target.getBoundingClientRect().x + radius;
  const centerY = event.target.getBoundingClientRect().y + radius;
  const deltaX = (event.targetTouches[0].clientX - centerX) / radius;
  const deltaY = (event.targetTouches[0].clientY - centerY) / radius;
  if (deltaX * deltaX + deltaY * deltaY > 1) {
    return;
  }
  const delta = (deltaX * deltaX + deltaY * deltaY);
  const maxSpeed = 50 + Math.min(delta * 1 / threshold100, 1) * 50;
  if (deltaX > 0 && deltaY > 0) {
    const amt = Math.atan2(deltaX, deltaY) * 4 / Math.PI - 1;
    action(amt * maxSpeed, -maxSpeed);
  } else if (deltaX < 0 && deltaY > 0) {
    const amt = - 1 - Math.atan2(deltaX, deltaY) * 4 / Math.PI;
    action(-maxSpeed, amt * maxSpeed);
  } else if (deltaX < 0 && deltaY < 0) {
    const amt = - 3 - Math.atan2(deltaX, deltaY) * 4 / Math.PI;
    action(amt * maxSpeed, maxSpeed);
  } else if (deltaX > 0 && deltaY < 0) {
    const amt = Math.atan2(deltaX, deltaY) * 4 / Math.PI - 3;
    action(maxSpeed, amt * maxSpeed);
  }

  console.log(deltaX, deltaY);
}

function Circle(props) {
  var circleStyle = {
    padding: 0,
    margin: 20,
    display: "inline-block",
    backgroundColor: props.color,
    borderRadius: "50%",
    width: 2 * radius,
    height: 2 * radius,
    left: 0,
    top: 0
  };
  return (
    // 
    <div onTouchStart={calculateMove} onTouchMove={calculateMove} onTouchCancel={() => action(0, 0)} onTouchEnd={() => action(0, 0)} style={circleStyle}>
    </div>
  );
}


function App() {
  useEffect(() => {
    document.addEventListener("touchmove", e => e.preventDefault(), { passive: false })
  });
  return (
    <div className="App">
      <div className="App-header" style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
        <img width={radius * 2} src="http://192.168.1.8:2201/video_feed" />
        <Circle color="#333437" />
      </div>
    </div>
  );
}

export default App;
