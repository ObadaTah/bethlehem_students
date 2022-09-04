
    head_sizer = document.querySelector(".head_sizer");
    xs = document.getElementsByName("xs")[0]
    s = document.getElementsByName("s")[0]
    m = document.getElementsByName("m")[0]
    l = document.getElementsByName("l")[0]
    xl = document.getElementsByName("xl")[0]
    xxl = document.getElementsByName("xxl")[0]

    xs_price = document.getElementById("xs_price")
    s_price = document.getElementById("s_price")
    m_price = document.getElementById("m_price")
    l_price = document.getElementById("l_price")
    xl_price = document.getElementById("xl_price")
    xxl_price = document.getElementById("xxl_price")

    if (xs.checked) {
        xs_price.disabled = false
    } else {
        xs_price.disabled = true
    }
    if (s.checked) {
        s_price.disabled = false
    } else {
        s_price.disabled = true
    }
    if (m.checked) {
        m_price.disabled = false
    } else {
        m_price.disabled = true
    }
    if (l.checked) {
        l_price.disabled = false
    } else {
        l_price.disabled = true
    }
    if (xl.checked) {
        xl_price.disabled = false
    } else {
        xl_price.disabled = true
    }
    if (xxl.checked) {
        xxl_price.disabled = false
    } else {
        xxl_price.disabled = true
    }

    xs.onclick = () => {
        if (xs.checked) {
            xs_price.disabled = false
            xs_price.required = true
        } else {
            xs_price.disabled = true
            xs_price.required = false
        }
    }
    s.onclick = () => {
        if (s.checked) {
            s_price.disabled = false
            s_price.required = true
            
        } else {
            s_price.disabled = true
            s_price.required = false
        }
    }
    m.onclick = () => {
        if (m.checked) {
            m_price.disabled = false
            m_price.required = true
            
        } else {
            m_price.disabled = true
            m_price.required = false
        }
    }
    l.onclick = () => {
        if (l.checked) {
            l_price.disabled = false
            l_price.required = true
            
        } else {
            l_price.disabled = true
            l_price.required = false
        }
    }
    xl.onclick = () => {
        if (xl.checked) {
            xl_price.disabled = false
            xl_price.required = true
            
        } else {
            xl_price.disabled = true
            xl_price.required = false
        }
    }
    xxl.onclick = () => {
        if (xxl.checked) {
            xxl_price.disabled = false
            xxl_price.required = true
            
        } else {
            xxl_price.disabled = true
            xxl_price.required = false
        }
    }


    inputs = document.querySelectorAll(".sizer")

    if (head_sizer.checked == false) {
        inputs.forEach((input) => {
            input.disabled = true
        })
    }


    head_sizer.onclick = () => {
        if (head_sizer.checked) {
            inputs.forEach((input) => {
                input.disabled = false
            })
            if (xxl.checked) {
                xxl_price.disabled = false
                xxl_price.required = true
            } else {
                xxl_price.disabled = true
                xxl_price.required = false
            }
            if (xl.checked) {
                xl_price.disabled = false
                xl_price.required = true
            } else {
                xl_price.disabled = true
                xl_price.required = false
            } if (l.checked) {
                l_price.disabled = false
                l_price.required = true
            } else {
                l_price.disabled = true
                l_price.required = false
            } if (m.checked) {
                m.disabled = false
                m.required = true
            } else {
                m_price.disabled = true
                m_price.required = false
            } if (s.checked) {
                sprice.disabled = false
                sprice.required = true
            } else {
                s_price.disabled = true
                s_price.required = false
            } if (xs.checked) {
                xs_price.disabled = false
                xs_price.required = true
            } else {
                xs_price.disabled = true
                xs_price.required = false
            }

        }
        else {
            xxl_price.disabled = true
            xl_price.disabled = true
            l_price.disabled = true
            m_price.disabled = true
            s_price.disabled = true
            xs_price.disabled = true
            
            xxl_price.required = false
            xl_price.required = false
            l_price.required = false
            m_price.required = false
            s_price.required = false
            xs_price.required = false

            inputs.forEach((input) => {
                input.disabled = true
            })
        }
    }
