export const fetchInfo  = async function (url, payload) {
    let options = {}
    if (payload) {
        options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        }
    } else {
        options = {
            method: 'GET'
        }
    }
    try {
        const response = await fetch(url, options)
        return await response.json()
    } catch (error) {
        console.error(error)
    }
}