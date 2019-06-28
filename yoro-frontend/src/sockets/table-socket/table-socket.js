import openSocket from "socket.io-client";

const socket = openSocket("http://4fd2bcd1.ngrok.io/lastCheckIn");
function subscribeToTimer(cb) {
  socket.on("lastCheckedInUser", timestamp => {
    console.log(timestamp);
    cb(null, timestamp);
  });
  socket.emit("subscribeToTimer", 10000);
}
export { subscribeToTimer };
