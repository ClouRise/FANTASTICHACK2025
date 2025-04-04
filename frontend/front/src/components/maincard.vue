    <template>
        <div>
            <header>
               <h2>{{ title }}</h2>
            </header>
            <main>
                <slot></slot>
            </main>
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
    
    </style>