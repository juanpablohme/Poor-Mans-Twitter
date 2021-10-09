<template>
    <div class="posts container">
        <Navbar></Navbar>
        <Postform></Postform>
        <div class="tweets-container">
            <div v-for="posts in APIData" :key="posts.id" class="tweet-card">
                <h5 class="name">{{posts.name}}</h5>
                <p class="content">{{posts.content}}</p>
                <p class="time">{{posts.date}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    import Postform from '../components/Postform'
    export default {
        name: 'Posts',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar,
            Postform
        },
        created() {
            getAPI.get('/posts/',)
                .then(response => {
                    console.log('Post API has recieved data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>

<style scoped>
.nav-bar {
    padding-top: 30px;
}
.posts {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.posts .tweets-container {
    width: 50%;
    display: flex;
    flex-direction: column-reverse;
}
.posts .tweet-card {
    width: 100%;
    padding: 20px 25px 10px 25px; 
    border: 1px solid rgba(0, 0, 0, 0.5);
    margin-bottom: 18px;
}
.posts .tweet-card .name {
    font-size: 1rem;
    text-decoration: underline;
    margin-bottom: 12px;
    display: inline-block;
}
.posts .tweet-card .time {
    font-size: 0.8rem;
    text-align: right;
}
</style>