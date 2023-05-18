const { nanoid } = require("nanoid");
const { Storage } = require("@google-cloud/storage");

const gcs = new Storage({
  projectId: "--project-id--",
  keyFilename: "servicekey.json",
});

const uploadImageHandler = async (request, h) => {
  try {
    const id = nanoid(8);
    const imageFile = request.payload.file;
    const filename = `${Date.now()}_${id}.jpg`;

    await gcs.bucket("--bucket-name--").upload(imageFile.path, {
      destination: filename,
    });

    const imageUrl = `https://storage.googleapis.com/sortify-img/${filename}`;

    return h.response({ imageUrl });
  } catch (error) {
    console.error("Error uploading image:", error);
    return h.response({ error: "Failed to upload image" }).code(500);
  }
};
module.exports = uploadImageHandler;
