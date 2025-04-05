    <template>
        <div class="card">
            <div class="header">
               <h2>{{ title }}</h2>
            </div>
            <div class="main">
                <slot></slot>
            </div>
        </div>
    </template>
    
    <script>
        export default {
            props: {
                title: {
                    type: String,
                    required: true
                }
            }
        }
    </script>
    
    <style scoped>
        .card{
            display: flex;
            flex-direction: column;
            padding: 20px;
        }
        .header{
            background-color: #2D2D2D;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: start;
            padding-inline: 35px;
        }
        .header h2{
            font-family: ubuntu-bold;
            color: white;
            font-size: 17px;
        }
        .main{
            background-color: #1D1D1D;
            border-radius: 0 0 15px 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            padding-top: 5px;
            padding-bottom: 20px;
            box-sizing: border-box;
        }
    </style>