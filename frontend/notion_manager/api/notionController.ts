import notionServices from "./notionServices";

const addItem = async (req, res) => {
    const { body } = req
    if (
        !body.text
    ) {
        res
            .status(400)
            .send({
                status: "FAILED",
                data: {
                    error:
                        "Error occurred because you failed to provide a clone key or a message"
                },
            });
        return;
    }
    const { title, summary, text, score } = body;
    const messageResponse =  await notionServices.addItem(title, summary, text, score);

    res.status(201).send({ status: "OK", data: {messageResponse} });
};

export default {
    addItem,
};