<template>
  <div class="hello">

    <ul>
      <li v-for="d in data">{{d.name}}</li>
    </ul>
    <input type="button" value="上一页" @click="pPage">

    <input type="button" value="下一页" v-on:click="nPage">
  </div>
</template>

<script>
  import merge from 'webpack-merge'
  import api from "../js/global"


  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        data: [],
        pageIndex: 1,
        pageSize: 15,
        over: false,
        showPageSum: 10 / 2,
        begin: 1,
        end: 11
      }
    },
    created() {
      if (this.$route.query.pageIndex) {
        this.pageIndex = parseInt(this.$route.query.pageIndex)
      }
      this.page()
      this.pagination()
      console.log(this.begin);
      console.log(this.end);
    },
    methods: {
      pagination() {
        if (this.pageIndex <= this.showPageSum / 2) {
          this.begin = 1
          this.end = this.showPageSum * 2
        } else {
          this.begin = this.pageIndex - this.showPageSum
          this.end = this.pageIndex + this.showPageSum
        }
      },
      pPage() {
        if (this.pageIndex == 1) {
          this.pageIndex = 1
          return
        }
        this.over = false
        this.pageIndex -= 1
        this.page()
        this.$router.push({
          query: merge(this.$route.query, {'pageIndex': this.pageIndex})
        })
      },
      nPage() {
        if (this.over) {
          return
        }
        this.pageIndex += 1
        this.page()
        this.$router.push({
          query: merge(this.$route.query, {'pageIndex': this.pageIndex})
        })
      },
      page() {
        this.axios({
          url: `${api}page/`,
          params: {
            pageIndex: this.pageIndex,
            pageSize: this.pageSize,
          }
        }).then((d) => {
          let data = d.data.data
          this.pageSum = d.data.pageSum
          this.data = data
          if (this.data.length < this.pageSize) {
            this.data.push({name: "没有更多数据L啦"})
            // this.page()
            // this.$router.push({
            //   query: merge(this.$route.query, {'pageIndex': this.pageIndex = 1})
            // })
            this.over = true
          } else {
            this.over = false
          }

        })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  * {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .pagination{
    /*display: inline-block;*/
  }
  .pagination li{
    display: inline-block;
    margin:10px;
  }

</style>
