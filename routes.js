const uploadImageHandler = require("./handler.js");

const routes = [
  {
    method: "POST",
    path: "/upload",
    options: {
      handler: uploadImageHandler,
      payload: {
        allow: "multipart/form-data",
        maxBytes: 209715200,
        multipart: true,
        output: "file",
      },
    },
  },
];

module.exports = routes;
