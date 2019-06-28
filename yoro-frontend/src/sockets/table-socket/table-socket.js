import openSocket from "socket.io-client";

const socket = openSocket("http://localhost:5000/lastCheckIn");
function subscribeToTimer(cb) {
  socket.on("lastCheckedInUser", timestamp => {
    console.log(timestamp);
    cb(null, timestamp);
  });
  socket.emit("subscribeToTimer", 10000);
}
export { subscribeToTimer };
