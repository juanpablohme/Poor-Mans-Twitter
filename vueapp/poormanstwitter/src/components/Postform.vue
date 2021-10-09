<template>
    <div class="form">
        <form @submit="postData" method="post">
            <input type="text" name="name" maxlength="20" placeholder="Name" required v-model="posts.name">
            <textarea type="text" name="content"  maxlength="50" placeholder="Message" required v-model="posts.content"></textarea>
            <button type="submit">Post</button>
        </form>
    </div>
</template>

<script>
    import Vue from 'vue'
    import axios from 'axios'
    import VueAxios from 'vue-axios'
    Vue.use(VueAxios, axios)

    export default {
        name: 'Postform',
        data () {
            return {
                posts: {
                    name: null,
                    content: null
                }
            }
        },
        methods: {
            postData(e) {
                e.preventDefault();

                let currentTime = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
                let jsonData = this.posts;
                jsonData.date = currentTime;

                this.axios.post('http://127.0.0.1:8000/api/posts/', this.posts)
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((err) => {
                        console.log(err);
                    })
                
            }      
        }
    }
</script>

<style scoped>
.form form {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
    justify-content: center;
}
.form input, .form textarea {
    margin-left: 10px;
    margin-right: 10px;
    padding: 10px;
    height: 50px;
    width: calc(50% - 20px);
}
.form button {
    display: block;
    width: calc(100% - 20px);
    margin-top: 15px;
    margin-bottom: 35px;
    height: 40px;    
}
</style>